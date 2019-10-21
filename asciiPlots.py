from ascii_graph import Pyasciigraph


# show plot for relative background radiations of each province
provRads = [ ('QC', 0.0016), ('NL', 0.0016), ('BC', 0.0018), ('ON', 0.0018), ('NB', 0.0018), ('PE', 0.0018), ('YT', 0.0019), 
	('NU', 0.0019), ('AB', 0.0024), ('NS', 0.0025), ('NT', 0.0031), ('SK', 0.0035), ('MB', 0.0041)
]
provRadsBar = Pyasciigraph(float_format='{:,.5f}')
for line in  provRadsBar.graph('Background radiations of every province', provRads):
    print(line)


test = [('long_label', 423), ('sl', 1234), ('line3', 531),
    ('line4', 200), ('line5', 834), ('max length line', 10000)]
graph = Pyasciigraph(float_format='{0:.0000f}')
for line in  graph.graph('test print', test):
    print(line)
