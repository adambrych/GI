import Readers.Tabl6_Reader as t6
import Readers.Tabl7_Reader as t7
import Readers.Tabl8_Reader as t8
import Readers.Tabl15_Reader as t15
import Readers.Tabl33_Reader as t33
import Readers.Tabl35_Reader as t35

def get_all():
    all_dict = dict()

    all_dict[t6.key] = t6.read_xlsx()
    all_dict[t7.key] = t7.read_xlsx()
    all_dict[t8.key] = t8.read_xlsx()
    all_dict[t15.key] = t15.read_xlsx()
    all_dict[t33.key] = t33.read_xlsx()
    all_dict[t35.key] = t35.read_xlsx()
    return all_dict
