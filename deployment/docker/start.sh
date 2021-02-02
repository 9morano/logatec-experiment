#!/bin/bash

# Set test
if [ "$TARGET" = "" ]; then
  echo "Target missing!"
else
  if [[ "$TARGET": = *"agent"* ]]; then
    # Set serial device
    if [ -z "$VESNA_DEV" ]; then
      echo "Serial device missing!"
    fi
  fi
  cd deployment/tasks/
  pwd 
  make "$TARGET"
fi