server = 'http://172.22.2.66:8080'
headers = {
        'content-type': "application/json;charset=UTF-8",
        'authorization': "Basic QVBJX2F1dG90ZXN0OkFQSV9hdXRvdGVzdA=="}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290"

get_user_list = '%s/SmiddleManager/adm/management/get_user_list' % server
add_user = '%s/SmiddleManager/adm/management/add_user' % server
delete_user = '%s/SmiddleManager/adm/management/delete_user'%server
edit_user = '%s/SmiddleManager/adm/management/edit_user' % server
post_user_group_roles = '%s/SmiddleManager/adm/management/user_group_roles' % server
get_aduser_list = '%s/SmiddleManager/adm/management/get_aduser_list' % server
get_task_list = '%s/SmiddleManager/adm/management/get_task_list' % server
set_tasks_to_role = '%s/SmiddleManager/adm/management/set_tasks_to_role' % server
get_role_access = '%s/SmiddleManager/adm/management/get_role_access' % server
edit_role = '%s/SmiddleManager/adm/management/edit_role' % server
add_role = '%s/SmiddleManager/adm/management/add_role' % server
delete_role = '%s/SmiddleManager/adm/management/delete_role' % server
add_group = '%s/SmiddleManager/adm/management/add_group' % server
edit_group = '%s/SmiddleManager/adm/management/edit_group' % server
delete_group = '%s/SmiddleManager/adm/management/delete_group' % server
Manager_logs = '%s/SmiddleManager/adm/admin/logs' % server
Manager_settings = '%s/SmiddleManager/adm/admin/settings' % server
test_domain = '%s/SmiddleManager/adm/admin/test_domain' % server
edit_domain = '%s/SmiddleManager/adm/admin/edit_domain' % server
delete_domain = '%s/SmiddleManager/adm/admin/delete_domain' % server
get_role_list = '%s/SmiddleManager/adm/management/get_role_list' % server
get_group_list = '%s/SmiddleManager/adm/management/get_group_list' % server
get_domain_list = '%s/SmiddleManager/adm/management/get_domain_list' % server
get_user_group_roles = '%s/SmiddleManager/adm/management/user_group_roles?user_id=16357506&group_id=1908533' % server
get_Manager_settings = '%s/SmiddleManager/adm/admin/settings' % server
Manager_manifest = '%s/SmiddleManager/adm/admin/manifest' % server
add_role_access = '%s/SmiddleManager/adm/management/add_role_access' % server
delete_role_access = '%s/SmiddleManager/adm/management/delete_role_access'% server

