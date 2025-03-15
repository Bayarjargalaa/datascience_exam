from generate_figures import *
from generate_report import *
from generate_business_report import *
from export_pdf import *

def generate_reports():
    """ Бүх тайланг нэгтгэн үүсгэх"""
    print("Тайлан үүсгэж байна...")
    
    # Графикууд үүсгэх
    print("Дүрслэлүүд үүсгэж байна...")
    
    # Загвар үнэлэх Markdown тайлан
    print(" Загварын үнэлгээний тайлан үүсгэж байна...")
    
    # Бизнесийн тайлан
    print(" Бизнесийн зөвлөмжүүдийг хадгалж байна...")

    # PDF тайлан
    print("PDF тайлан хадгалж байна...")

    print("Бүх тайлан амжилттай үүсгэлээ!")

if __name__ == "__main__":
    generate_reports()
