# metabook

One metadata entry for every book

## Index

- [Background](#background)
- [Installation](#installation)

## Background

The Internet Archive has millions of digitized books. Over 2M of the
Internet Archive's books have
[OCLC](https://www.oclc.org/home.en.html) identifiers.  For books
which have been resolved to their OCLC identifiers, Alexis Rossi has
provided a [book linked-data flow
diagram](http://www.alexisrossi.com/linked-book-data/) which documents
how metadata from different sources can also be retrieved, depending
on what identifiers you have available.

The goal of this project is to leverage whatever remote identifiers we
have available (e.g. Amazon's "asin") to resolve a book to as many of
its qualified remote sources as possible, and to coalesce each
source's metadata into a single coherent, complete metadata record.

## Installation

    $ git clone https://github.com/ArchiveLabs/metabook.git
    $ cd metabook
    $ pip install .

## Usage

Metabook will have a command line interface called `metabook` which
has not yet been documented.

## Supported Sources

- OCLC [No]
- Wikidata [No]
- OpenLibrary [No]
- VIAF [No]
- Amazon [No]
- Goodreads [No]
- LibraryThing [No]
