import pywebio
from pywebio.output import put_html

import msg
import menu

multiprocessing = '***' * 11
put_html(multiprocessing)
put_html(msg.GREETINGS)
put_html(multiprocessing)

