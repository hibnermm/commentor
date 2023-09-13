from django.contrib import admin
class CommentorAdminSite(admin.AdminSite):
  title_header = 'Commentor Admin'
  site_header = 'Commentor administration'
  index_title = 'Commentor site admin'
  logout_template = 'commentor/logged_out.html'