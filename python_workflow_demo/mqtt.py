# -*- coding: utf-8 -*-
#
# Copyright (c) 2017, Leigh McKenzie
# All rights reserved.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


import asyncio
import paho.mqtt.client as paho_client

_client = paho_client.Client()
_connected = False
_subscribers = []


def connect():
    _client.connect(host='test.mosquitto.org', port=1883, keepalive=60, bind_address='')


def disconnect():
    pass


def reconnect():
    pass


def publish(topic, data, options):
    _client.publish(topic, data)


def subscribe(topic, handler, options=None):
    options = options or {}
    _subscribers.append(
        {
            'topic': topic,
            'handler': handler,
            'options': options
        }
    )

    if _connected:
        _client.subscribe(topic)


# The callback for when the client receives a CONNACK response from the server.
def _on_connect(client, userdata, flags, rc):
    _connected = True
    print("Connected with result code " + str(rc))

    for subscriber in _subscribers:
        client.subscribe(subscriber['topic'])


        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        # client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def _on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

    for subscriber in _subscribers:
        if paho_client.topic_matches_sub(sub=subscriber['topic'], topic=msg.topic):
            subscriber['handler'](msg.payload)


# Called when the client disconnects from the broker.
def on_disconnect(client, userdata, rc):
    _connected = False


_client.on_connect = _on_connect
_client.on_message = _on_message


def run():
    _client.loop(timeout=0)
    asyncio.get_event_loop().call_later(1.0, run)
