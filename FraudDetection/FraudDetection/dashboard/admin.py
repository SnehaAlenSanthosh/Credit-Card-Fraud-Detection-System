from django.contrib import admin
from .models import Data
admin.site.site_header = 'Credit Card Fraud Detection - Administration'
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('time', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17', 'v18', 'v19', 'v20', 'v21','v22', 'v23', 'v24', 'v25', 'v26', 'v27', 'v28','amount', 'predictions')

admin.site.register(Data, DataAdmin)
