# Design rationale

I separated the command-line interface from the calculation and storage code so each part has a clear responsibility. `cli.py` reads commands and prints results; `services.py` adds transactions and calculates balances; `validation.py` rejects bad inputs; and `storage.py` handles JSON persistence. This structure makes the program easier to test without repeatedly typing commands, and it helps prevent invalid records from being saved. I chose JSON for the working file because it preserves structured records and can be read again after the program exits.
