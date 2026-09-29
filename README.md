# Inventory Reorder Check

A Python script that checks hardware store stock levels and flags what needs reordering.

## What it does
- Stores stock for a set of items in a dictionary
- Checks each item against a reorder threshold (currently 70 units)
- Prints OK or REORDER NEEDED for each item
- Prints total count of items that need reordering

## What it doesn't do yet
- Doesn't update stock — this only reads and reports, it's not live
- Doesn't save between runs — data is hardcoded for now
- No unit column yet (quantity only — planning to add units like pcs/kg/m next)
- Same threshold for every item, not item-specific

## Why I built it
I run Jai Shree Shyam Traders, a hardware store, and manage stock through TallyPrime day to day. This project isn't replacing that — it's practice applying Python to a real inventory problem I understand, as a step toward building tools that could eventually connect to or complement systems like Tally (e.g., pulling data out and flagging reorder needs automatically).

## Tech used
Python — dictionaries, loops, conditionals, f-strings