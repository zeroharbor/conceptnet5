import click
from . import (
    conceptnet4, globalmind, jmdict, nadya, ptt_petgame, umbel, verbosity,
    wiktionary, wordnet
)


@click.group()
def cli():
    pass


@cli.command(name='conceptnet4')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_conceptnet4(input, output):
    """
    Import a file of data exported from ConceptNet 4.

    input: a .jsons file of ConceptNet 4 data
    output: a msgpack file of edges
    """
    conceptnet4.handle_file(input, output)


@cli.command(name='globalmind')
@click.argument('input_dir',
                type=click.Path(readable=True, dir_okay=True, file_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_globalmind(input_dir, output):
    """
    Import a file of data exported from GlobalMind.

    input_dir: a directory containing .jsons files exported from GlobalMind
    output: a msgpack file of edges
    """
    globalmind.handle_file(input_dir, output)


@cli.command(name='jmdict')
@click.argument('input', type=click.Path(readable=True, dir_okay=False),
                #help='XML file containing JMDict'
                )
@click.argument('output', type=click.Path(writable=True, dir_okay=False),
                #help='msgpack file to output to'
                )
def run_jmdict(input, output):
    """
    Import JMDict (a multilingual Japanese dictionary) from its XML format.

    input: the path to JMDict.xml
    output: a msgpack file of edges
    """
    jmdict.handle_file(input, output)


@cli.command(name='nadya')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_nadya(input, output):
    """
    Import a file of data exported from nadya.jp.

    input: a file of comma-separated nadya.jp data
    output: a msgpack file of edges
    """
    nadya.handle_file(input, output)


@cli.command(name='ptt_petgame')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_ptt_petgame(input, output):
    """
    Import a file of data exported from the "Pet Game", a game about teaching
    and sharing common-sense knowledge that was hosted on PTT for a while.
    (PTT is a BBS-like system that was extremely popular in Taiwan in the
    decade of the 2000s.)

    input: a file of tab-separated Pet Game data
    output: a msgpack file of edges
    """
    ptt_petgame.handle_file(input, output)


@cli.command(name='umbel')
@click.argument('input_dir',
                type=click.Path(readable=True, dir_okay=True, file_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
@click.option('--mapping', '-m', type=click.Path(writable=True, dir_okay=False),
              help='write a mapping of Semantic Web URIs to this file')
def run_umbel(input_dir, output, mapping):
    """
    Import data from Umbel, a Semantic Web-ish wrapper around structured
    ontologies such as OpenCyc.

    input_dir: a directory containing N-Triples files of Umbel data
    output: a msgpack file of edges
    mapping: an N-Triples output file that will map external Semantic Web URIs to
      ConceptNet URIs
    """
    umbel.handle_file(input_dir, output, mapping)


@cli.command(name='verbosity')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_verbosity(input, output):
    """
    Import a file of data exported from Verbosity, a Taboo-like game for
    collecting common sense knowledge, run by CMU's Games with a Purpose
    project.

    input: a file of tab-separated Verbosity data
    output: a msgpack file of edges
    """
    verbosity.handle_file(input, output)


@cli.command(name='wiktionary_pre')
@click.argument('inputs', type=click.Path(readable=True, dir_okay=False),
                nargs=-1)
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_wiktionary_pre(inputs, output):
    """
    Build a SQLite DB that extracts data from our parsed version of Wiktionary.
    This DB will be used in later steps, including the actual Wiktionary import.

    inputs: several files of parsed Wiktionary data, as gzipped JSON streams
    output: the SQLite DB to write to
    """
    wiktionary.prepare_db(inputs, output)


@cli.command(name='wiktionary')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('db', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_wiktionary(input, db, output):
    wiktionary.read_wiktionary(input, db, output)


@cli.command(name='wordnet')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
@click.option('--mapping', '-m', type=click.Path(writable=True, dir_okay=False))
def run_wordnet(input, output, mapping):
    """
    Import a file of N-Triples data from WordNet-RDF, a Linked Data version of
    Open Multilingual WordNet.

    input: an .nt file of WordNet data
    output: a msgpack file of edges
    mapping: an N-Triples output file that will map external Semantic Web URIs to
      ConceptNet URIs
    """
    wordnet.handle_file(input, output, mapping)
