import pandas as pd
import numpy as np
from scipy.sparse import load_npz
from scipy.sparse import save_npz
from scipy import sparse
import igraph

# load direct citation networks
g_by_2015 = igraph.Graph.Read("citation_by_2015.graphml", format="graphml")
g_by_2010 = igraph.Graph.Read("citation_by_2010.graphml", format="graphml")
