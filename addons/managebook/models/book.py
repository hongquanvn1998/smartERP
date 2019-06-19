# -*- coding: utf-8 -*-

from odoo import models,fields

class Book(models.Model):
    _name = "managebook.mybook"
    _rec_name = "name_book" #tên hiển thị trên quan hệ many2many, one2many, many2one
    _auto = True #tự động tạo bảng nếu bằng True
    _table = u'Các cuốn sách' #tên hiển thị khi truy cập vào bảng
    _description = u'Sách của tui' #mô tả bảng
    _order = 'author_main,name_book' #sắp xếp thứ tự các trường trong bảng
    _translate = True #cho phép dịch sang ngôn ngữ khác

    name_book = fields.Char(string="Tên sách", size=200,translate=True,default="")
    image = fields.Binary("Hình ảnh")
    date_publication = fields.Date("Ngày xuất bản")
    quantum =  fields.Integer(string="Số lượng")
    publisher = fields.Selection(
        string="Nhà xuất bản",
        selection=[('0','Kim Đồng'),('1',"Tuổi trẻ"),('2','Thanh niên'),('3','Bộ giáo dục & Đào tạo')]
    )
    description = fields.Char(string="Ghi chú")
    number_page = fields.Integer(string="Số trang")
    description = fields.Text("Mô tả",help="viết mô tả ở đây")
    author_main = fields.Many2one(comodel_name="managebook.author",string="Tác giả chính",required=True)
    author_2nd = fields.Many2one(comodel_name="managebook.author",string="Tác giả phụ")


    _sql_constraints = {('ten_sach_la_duy_nhat','UNIQUE(name_book)',u'Sách bạn tạo đã tồn tại vui lòng thử lại')}
    _depends = {} #truy xuất dữ liệu đến các bảng để lấy fields,model