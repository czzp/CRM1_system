from django.conf.urls import url, include

from crm import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^index/$', views.index),
    url(r'^index/getuser/$', views.getUser),
    url(r'^index/addCustomer/$', views.addCustomer),
    url(r'^index/getCustomer/$', views.getCustomer),
    # url(r'^index/queryCustomer/$', views.queryCustomer),
    url(r'^index/updateCustomer/$', views.updateCustomer),
    url(r'^index/editCustomer/$', views.editCustomer),
    url(r'^index/delCustomer/$', views.delCustomer),
    url(r'^index/noticeDel/(\d*)/$', views.noticeDel),
    url(r'^index/noticeAdd/$', views.noticeAdd),
    url(r'^index/noticeQuery/$', views.noticeQuery),
    url(r'^index/get_userNum/$', views.get_userNum),
    url(r'^index/userAdd/$', views.userAdd),
    url(r'^index/roleAdd/$', views.roleAdd),
    url(r'^index/userRoleDel/$', views.userRoleDel),
    url(r'^index/departmentAdd/$', views.departmentAdd ,name= 'departmentAdd'),
    url(r'^index/departmentDel/$', views.departmentDel,name= 'departmentDel'),
    url(r'^customer_list1.html/(\d*)/$', views.pageCustomer),
    url(r'^customer_list2.html/(\d*)/$', views.queryCustomer),
    url(r'^(.*?)/$', views.others),
    ]
