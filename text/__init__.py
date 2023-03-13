""" from https://github.com/keithito/tacotron """
from text import cleaners
import numpy
from text.symbols import symbols
# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}

def text_to_sequence(text, symbols, cleaner_names):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  _symbol_to_id = {s: i for i, s in enumerate(symbols)}

  sequence = []
  clean_text = _clean_text(text, cleaner_names)
  for symbol in clean_text:
    if symbol not in _symbol_to_id.keys():
      continue
    symbol_id = _symbol_to_id[symbol]
    sequence += [symbol_id]
  tone = numpy.zeros_like(sequence)
  return sequence, tone

def cleaned_text_to_sequence(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = [_symbol_to_id[symbol] for symbol in cleaned_text if symbol in _symbol_to_id.keys()]
  tone = numpy.zeros_like(sequence)
  return sequence, tone

def sequence_to_text(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = [_id_to_symbol[symbol] for symbol in cleaned_text if symbol in _id_to_symbol.keys()]
  return sequence

def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    cleaner = getattr(cleaners, name)
    if not cleaner:
      raise Exception('Unknown cleaner: %s' % name)
    text = cleaner(text)
  return text
