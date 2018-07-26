from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Danh sách lớp chưa hoàn thiện !! "

@app.route('/user/<username>')
def get_info_user(username):
    users ={
    
        'quan': {
            'name': 'Nguyễn Anh Quân',
            'age': 16
            },

        'tuananh': {
            'name': 'Huỳnh Tuấn Anh',
            'age': 23
            },

        'huyen': {
            'name': 'Hoàng Thanh Huyền',
            'age': 15
            },

        'lien': {
            'name': 'Phẫn Kim Liên ',
            'age': 18
            },

        'ngocanh': {
            'name': 'Nguyễn Ngọc Anh',
            'age': 23
            },

        'nhung': {
            'name': 'Nguyễn Hồng Nhung',
            'age': 21
            },

        'linh': {
            'name': 'Việt Linh',
            'age': 19
            },

        'ha': {
            'name': 'Anh Hà',
            'age': 21
            },

        'thu': {
            'name': 'Bạn Thu',
            'age': 18
            },

        'dieu': {
            'name': 'Bạn Diệu',
            'age': 21
            },

        'phuong': {
            'name': 'Chị Phương',
            'age': 21
            },

        'hoang': {
            'name': 'Anh Hoàng',
            'age': 21
            }
        }
    if username not in users:
        return("Error: User not found !!!")
    else:
        return render_template("index.html", users= users, username= username)
    

if __name__ == '__main__':
  app.run(debug=True)
 