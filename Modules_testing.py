import time
a = time.time()
import Modules_n_Packages.ari_ops.ari as ar
import Modules_n_Packages.str_ops.str_oprs as st
print(ar.add(4,5))
print(st.cat("4","5"))
print(abs(a - time.time())*1000)

from Modules_n_Packages.str_ops import str_oprs as st
print(st.cat("gf","ged"))