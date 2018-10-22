"""Improved Color Kafka"""

import argparse
import atexit
import json
import os
import sys
from datetime import datetime
from ickafka.__version__ import version
from kafka import KafkaConsumer
from pygments import highlight
from pygments.formatters import TerminalFormatter  # pylint: disable-msg=E0611
from pygments.lexers import JsonLexer  # pylint: disable-msg=E0611


def main():
    # parse the args
    parser = argparse.ArgumentParser(description="Consume from kafka")
    parser.add_argument(
        "-s", "--server", help="kafka broker ip or hostname", default="localhost"
    )
    parser.add_argument("-g", "--group", help="kafka consumer group", default=None)
    parser.add_argument(
        "-o",
        "--offset",
        help="which offset to start at. options: smallest, earliest, latest",
        default="latest",
    )
    parser.add_argument("-t", "--topic", help="kafka topic name", required=True)
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=version,
        help="ickafka version",
        default=None,
    )
    args = parser.parse_args()

    # start consuming them bytes
    consumer = KafkaConsumer(
        args.topic,
        auto_offset_reset=args.offset,
        bootstrap_servers=[args.server],
        enable_auto_commit=True,
        group_id=args.group,
    )

    global captured_messages
    captured_messages = []

    # print each message that is consumed
    for count, message in enumerate(consumer, 1):
        message = message.value.decode("utf-8")
        try:
            message = json.loads(message)
            message = json.dumps(message, indent=4, sort_keys=True)
            print(highlight(message, JsonLexer(), TerminalFormatter()))
            captured_messages.append(json.loads(message))
        except Exception:  # pylint: disable=broad-except
            print(message)
            captured_messages.append(message)
        print("message count: {}".format(count))


def exit_handler():
    json_dumped_file = "ickafka_dump_%s.json" % datetime.utcnow().isoformat()
    print("")
    print("Dumping consumed messages into: %s" % json_dumped_file)
    print("")
    with open(json_dumped_file, "w") as outfile:
        json.dump(captured_messages, outfile)
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


atexit.register(exit_handler)

try:
    main()

except KeyboardInterrupt:
    exit_handler()
