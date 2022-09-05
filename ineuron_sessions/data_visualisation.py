# Aug 13 2022 session
import cufflinks as cf
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.offline
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
cf.go_offline()
# cf.set_config_file(offline=True, offline_connected=False, offline_show_link=True, world_readable=True)


df = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])
# print(df)


# df.iplot()
