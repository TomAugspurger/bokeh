''' Mix-in classes that bulk add groups of properties to Bokeh models.

Some groups of properties often show up in Bokeh models together. For
instance, any model that exposes a fill color property for use when
rendering will almost always want to expose a fill alpha as well. To
reduce boilerplate code and simplify defining models with these sets
of properties, use the mix-in classes in this module:

* |FillProps| --- properties for fill color and alpha

* |LineProps| --- properties for line color, dashing, width, etc.

* |TextProps| --- properties for text color, font, etc.

To include these properties in a Bokeh model, use the |Include| property
as shown here:

.. code-block:: python

    class SomeGlyph(Glyph):

        fill_props = Include(FillProps, use_prefix=False, help="""
        The %s values for the annular wedges.
        """)

This adds all the fill properties ``fill_color`` and ``fill_alpha`` to this
model with one simple statement. Note that the help string contains a
placeholder format `%s`. When docs for this class are rendered by the
:ref:`bokeh.sphinxext.bokeh_model` Sphinx extension, the placeholder will
be replaced with more information specific to each property. The setting
``use_prefix`` means that the names of the properties added to ``SomeGlyph``
are exactly ``fill_alpha`` and ``fill_color``. Some situations require a
different usage, for more information see the docs for |Include|.

.. |Include| replace:: :class:`~bokeh.core.properties.Include`

.. |FillProps| replace:: :class:`~bokeh.core.property_mixins.FillProps`
.. |LineProps| replace:: :class:`~bokeh.core.property_mixins.LineProps`
.. |TextProps| replace:: :class:`~bokeh.core.property_mixins.TextProps`

'''
from __future__ import absolute_import

from .enums import LineJoin, LineCap, FontStyle, TextAlign, TextBaseline
from .has_props import HasProps
from .properties import ColorSpec, DashPattern, Enum, FontSizeSpec, Int, NumberSpec, String, value

class FillProps(HasProps):
    ''' Properties relevant to rendering fill regions.

    Mirrors the BokehJS ``properties.Fill`` class.

    '''

    fill_color = ColorSpec(default="gray", help="""
    A color to use to fill paths with.

    Acceptable values are:

    - any of the 147 named `CSS colors`_, e.g ``'green'``, ``'indigo'``
    - an RGB(A) hex value, e.g., ``'#FF0000'``, ``'#44444444'``
    - a 3-tuple of integers (r,g,b) between 0 and 255
    - a 4-tuple of (r,g,b,a) where r,g,b are integers between 0..255 and a is between 0..1

    .. _CSS colors: http://www.w3schools.com/cssref/css_colornames.asp

    """)

    fill_alpha = NumberSpec(default=1.0, help="""
    An alpha value to use to fill paths with.

    Acceptable values are floating point numbers between 0 (transparent)
    and 1 (opaque).

    """)

class LineProps(HasProps):
    ''' Properties relevant to rendering path operations.

    Mirrors the BokehJS ``properties.Line`` class.

    '''

    line_color = ColorSpec(default="black", help="""
    A color to use to stroke paths with.

    Acceptable values are:

    - any of the 147 named `CSS colors`_, e.g ``'green'``, ``'indigo'``
    - an RGB(A) hex value, e.g., ``'#FF0000'``, ``'#44444444'``
    - a 3-tuple of integers (r,g,b) between 0 and 255
    - a 4-tuple of (r,g,b,a) where r,g,b are integers between 0..255 and a is between 0..1

    .. _CSS colors: http://www.w3schools.com/cssref/css_colornames.asp

    """)

    line_width = NumberSpec(default=1, help="""
    Stroke width in units of pixels.
    """)

    line_alpha = NumberSpec(default=1.0, help="""
    An alpha value to use to stroke paths with.

    Acceptable values are floating point numbers between 0 (transparent)
    and 1 (opaque).

    """)

    line_join = Enum(LineJoin, help="""
    How path segments should be joined together.

    Acceptable values are:

    - ``'miter'`` |miter_join|
    - ``'round'`` |round_join|
    - ``'bevel'`` |bevel_join|

    .. |miter_join| image:: /_images/miter_join.png
       :height: 15
    .. |round_join| image:: /_images/round_join.png
       :height: 15
    .. |bevel_join| image:: /_images/bevel_join.png
       :height: 15

    """)

    line_cap = Enum(LineCap, help="""
    How path segments should be terminated.

    Acceptable values are:

    - ``'butt'`` |butt_cap|
    - ``'round'`` |round_cap|
    - ``'square'`` |square_cap|

    .. |butt_cap| image:: /_images/butt_cap.png
       :height: 12
    .. |round_cap| image:: /_images/round_cap.png
       :height: 12
    .. |square_cap| image:: /_images/square_cap.png
       :height: 12

    """)

    line_dash = DashPattern(help="""
    How should the line be dashed.
    """)

    line_dash_offset = Int(0, help="""
    The distance into the ``line_dash`` (in pixels) that the pattern should
    start from.
    """)

class TextProps(HasProps):
    ''' Properties relevant to rendering text.

    Mirrors the BokehJS ``properties.Text`` class.

    .. note::
        There is currently only support for filling text. An interface
        to stroke the outlines of text has not yet been exposed.

    '''

    text_font = String("helvetica", help="""
    Name of a font to use for rendering text, e.g., ``'times'``,
    ``'helvetica'``.

    """)

    text_font_size = FontSizeSpec(value("12pt"))

    text_font_style = Enum(FontStyle, help="""
    A style to use for rendering text.

    Acceptable values are:

    - ``'normal'`` normal text
    - ``'italic'`` *italic text*
    - ``'bold'`` **bold text**

    """)

    text_color = ColorSpec(default="#444444", help="""
    A color to use to fill text with.

    Acceptable values are:

    - any of the 147 named `CSS colors`_, e.g ``'green'``, ``'indigo'``
    - an RGB(A) hex value, e.g., ``'#FF0000'``, ``'#44444444'``
    - a 3-tuple of integers (r,g,b) between 0 and 255
    - a 4-tuple of (r,g,b,a) where r,g,b are integers between 0..255 and a is between 0..1

    .. _CSS colors: http://www.w3schools.com/cssref/css_colornames.asp

    """)

    text_alpha = NumberSpec(default=1.0, help="""
    An alpha value to use to fill text with.

    Acceptable values are floating point numbers between 0 (transparent)
    and 1 (opaque).

    """)

    text_align = Enum(TextAlign, help="""
    Horizontal anchor point to use when rendering text.

    Acceptable values are:

    - ``'left'``
    - ``'right'``
    - ``'center'``

    """)

    text_baseline = Enum(TextBaseline, default="bottom", help="""
    Vertical anchor point to use when rendering text.

    Acceptable values are:

    - ``'top'``
    - ``'middle'``
    - ``'bottom'``
    - ``'alphabetic'``
    - ``'hanging'``
    - ``'ideographic'``

    """)
