import Readers.Tabl6_Reader as t6
import Readers.Tabl7_Reader as t7
import Readers.Tabl8_Reader as t8
import Readers.Tabl15_Reader as t15
import Readers.Tabl33_Reader as t33
import Readers.Tabl35_Reader as t35

def get_all():
    file_name = "2009.xls"
    t6.get_one(file_name)
    t7.get_one(file_name)
    t8.get_one(file_name)
    t15.get_one(file_name)
    t33.get_one(file_name)
    t35.get_one(file_name)

get_all()
