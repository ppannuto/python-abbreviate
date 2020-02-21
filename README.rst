Abbreviate
==========

This filter attempts to automatically and intelligently abbreviate strings.

This library contains a dictionary of known abbreviations. Some words have
multiple abbreviations, e.g. Thursday could be abbreviated as any of Thurs,
Thur, Thr, Th, or T depending on context. With no other information, each word
has a "preferred abbreviation" (Thr), however options can push things one way
or another. For words without known abbreviations, a series of heuristics are
applied to shorten them as needed.

The basic `abbreviate` method will only apply preferred abbreviations and
no heuristics. For more advanced applications, the library can be given a
target length and effort, and will attempt to generate the best string
possible. Length can be supplied either as a simple character count, or with a
custom length function. The latter is useful in many graphics applications
without monospaced fonts or constant kerning. By default, abbreviate will not
shorten any exisiting abbreviations (e.g. Thur -> Th), assuming that any
explicit abbreviation was passed as such for a reason.

Issues, updates, pull requests, etc should be directed
`to github <https://github.com/ppannuto/python-abbreviate>`_.


State
-----

This tool was written to scratch an immediate itch and is thus quite
incomplete, but with extensibility and somewhat grander ideas in mind.
Architectural thoughts, radical changes to methodology, or just greater
abbreviations are all welcome.

Installation
------------

The easiest method is to simply use pip:

::

    (sudo) pip install abbreviate

Usage
-----

.. code-block:: python

 >>> import abbreviate
 >>> abbr = abbreviate.Abbreviate()
 
 >>> abbr.abbreviate("This library does nothing without pressure to make shorter")
 'This library does nothing without pressure to make shorter'
 
 >>> abbr.abbreviate("By default, it will treat length as simple character count", 20)
 'By dflt, it wll trt lngth as smple chrctr cnt'
 
 >>> from reportlab.lib.units import inch
 >>> from reportlab.pdfgen import canvas
 >>> from reportlab.lib.pagesizes import letter
 >>> c = canvas.Canvas('/tmp/example.pdf', pagesize=letter)
 >>> def calculate_rendered_length(text):
 ...     return c.stringWidth(text, "Helvetica", 8)
 >>> abbr.abbreviate("A custom length function is useful for rendered text", target_len=2.5*inch, len_fn=calculate_rendered_length)
 'A cstm length function is useful for rendered text'
