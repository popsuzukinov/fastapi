from controllers import *
app.add_api_route('/', index)

# urls.py
# FastAPIのルーティング用関数
app.add_api_route('/', index)
app.add_api_route('/admin', admin)  # new
