# You can control the number of replacements by specifying the count parameter:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)