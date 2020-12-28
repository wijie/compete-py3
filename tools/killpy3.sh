#!/bin/sh

ps -ax | grep python | cut -c1-5 | xargs kill
