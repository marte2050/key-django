#!/bin/bash

poetry install
tail -f /dev/null # garante que o container não será finalizado