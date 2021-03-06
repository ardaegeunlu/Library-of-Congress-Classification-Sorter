# Library-of-Congress-Classification-Sorter

## Arrange Books in Call Number Order Using the Library of Congress System 
The implementation follows this [brief guide.](https://www.libraries.rutgers.edu/rul/staff/access_serv/student_coord/LibConSys.pdf)

## Example 

```python
import functools
from lcc_sort_helpers import LCCSortComparison

call_number_list.sort(key=functools.cmp_to_key(LCCSortComparison))
```

A small sorted file is attached as an example output.

A brief snapshot:

* HJ2051.W483 2001
* HJ2053.A1T48 2001
* HJ2053.A1U54 2000
* HJ2053.C3C35 2000
* HJ2053.M2S72 2000
* HJ2053.M2S73 1999
* HJ2053.S724 1999
* HJ2053.T5T44 1999
* HJ2053.W2L44 1999
* HJ2053.W8W96 1999
* HJ2054.C36 1999
* HJ2056.5.Q3P76 1999
* HJ2066.M46 1999
* HJ2075.B87 2000
* HJ2094.E53 1997
* HJ2094.G67 1999
* HJ2094.M49 2000
* HJ2105.B72 1999
* HJ2108.C585 2001
* HJ2130.7.E76 1999
* HJ2130.7.I24 1999
* HJ2132.S43 1999
* HJ2139.B65 2000
* HJ2151.4.O94 2000
* HJ2152.P47 1990
* HJ2152.S56 1992
* HJ2157.C46 2001
* HJ2157.R34 2000
* HJ2158.G6O73 1999
* HJ2158.5.E83 2000
* HJ2158.6.B35B83 2000
* HJ2162.6.M35 2000
* HJ2179.8.S83 1997
* HJ2180.9.G68 1996
* HJ2181.2.M328 2000
* HJ2181.2.M33 2000
* HJ2181.4.W35 1999
* HJ2181.4.Z9G384 1998
* HJ2181.9.C66 1990
* HJ2184.7.A54 1996
* HJ2184.7.A74 1998
* HJ2184.7.A96 2000
* HJ2184.7.G34 1997
* HJ2305.G55 2000
