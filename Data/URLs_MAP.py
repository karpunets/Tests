server = 'http://172.22.2.66:8080'
# headers = {
#     'content-type': "application/json;charset=UTF-8",
#     'authorization': "Basic QVBJX2F1dG90ZXN0X1JPT1Q6QVBJX2F1dG90ZXN0X1JPT1Q="}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290"
# authorization = ('API_autotest_ROOT', 'API_autotest_ROOT')

headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290"
authorization = ('Root', 'Smidle098adm!')


ROOT = "Basic QVBJX2F1dG90ZXN0X1JPT1Q6QVBJX2F1dG90ZXN0X1JPT1Q="
ADMINISTRATOR = "Basic QVBJX2F1dG90ZXN0X0FETUlOSVNUUkFUT1I6QVBJX2F1dG90ZXN0X0FETUlOSVNUUkFUT1I="
USER = "Basic QVBJX2F1dG90ZXN0X1VTRVI6QVBJX2F1dG90ZXN0X1VTRVI="
SUPERVISOR = "Basic QVBJX2F1dG90ZXN0X1NVUEVSVklTT1I6QVBJX2F1dG90ZXN0X1NVUEVSVklTT1I="
# ADMIN
get_user_list = '%s/SmiddleManager/adm/management/get_user_list' % server
add_user = '%s/SmiddleManager/adm/management/add_user' % server
delete_user = '%s/SmiddleManager/adm/management/delete_user' % server
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
delete_role_access = '%s/SmiddleManager/adm/management/delete_role_access' % server

# CAMPAIGN MANAGER UCCE
get_campaign = '%s/SmiddleCampaignManager/cm/manager/get_campaign' % server
get_batch = '%s/SmiddleCampaignManager/cm/manager/get_batch' % server
get_dial_list = '%s/SmiddleCampaignManager/cm/dialer/get_dial_lists' % server
check_campaign_status = '%s/SmiddleCampaignManager/cm/dialer/check_campaign_status' % server
get_result_code = '%s/SmiddleCampaignManager/cm/manager/get_result_code' % server
edit_batch = '%s/SmiddleCampaignManager/cm/manager/edit_batch' % server
get_mapfields = '%s/SmiddleCampaignManager/cm/settings/get_mapfields' % server
edit_result_code = '%s/SmiddleCampaignManager/cm/manager/edit_result_code' % server
get_result_variants = '%s/SmiddleCampaignManager/cm/manager/get_result_variants' % server
edit_result_variant = '%s/SmiddleCampaignManager/cm/manager/edit_result_variant' % server
map_field = '%s/SmiddleCampaignManager/cm/settings/map_field' % server
edit_campaign = '%s/SmiddleCampaignManager/cm/manager/edit_campaign' % server
edit_dial_list = '%s/SmiddleCampaignManager/cm/dialer/edit_dial_list' % server
get_personal_callback = '%s/SmiddleCampaignManager/cm/dialer/get_personal_callback' % server
start_campaign = '%s/SmiddleCampaignManager/cm/dialer/start_campaign' % server
get_cd_status = '%s/SmiddleCampaignManager/cm/dialer/get_cd_results' % server
stop_campaign = '%s/SmiddleCampaignManager/cm/dialer/stop_campaign' % server
get_settings = '%s/SmiddleCampaignManager/cm/admin/settings' % server
get_skillgroup_list = '%s/SmiddleCampaignManager/cm/dialer/get_skillgroup_list' % server
get_timezone_list = '%s/SmiddleCampaignManager/cm/dialer/get_timezone_list' % server
get_fixed_fields = '%s/SmiddleCampaignManager/cm/settings/get_fixed_fields' % server
remove_result_code = '%s/SmiddleCampaignManager/cm/manager/remove_result_code' % server
delete_mapfield = '%s/SmiddleCampaignManager/cm/settings/delete_mapfield' % server
delete_dial_list = '%s/SmiddleCampaignManager/cm/dialer/delete_dial_list' % server
delete_campaign = '%s/SmiddleCampaignManager/cm/manager/delete_campaign' % server
remove_result_variant = '%s/SmiddleCampaignManager/cm/manager/remove_result_variant' % server


# CAMPAIGN MANAGER UCCX


# SMART_CALL_BACK
fixed_routes = "%s/SmiddleSmartCallback/scb/route/fixed" % server
soft_routes = "%s/SmiddleSmartCallback/scb/route/soft" % server
route_filter = "%s/SmiddleSmartCallback/scb/call/filter" % server
scb_manifest = "%s/SmiddleSmartCallback/scb/manifest" % server
scb_licenses = "%s/SmiddleSmartCallback/scb/licenses" % server
scb_count = "%s/SmiddleSmartCallback/scb/licenses/rt/count" % server
scb_settings = "%s/SmiddleSmartCallback/scb/settings" % server
scb_contact = "%s/SmiddleSmartCallback/scb/contact" % server
scb_statistic = "%s/SmiddleSmartCallback/scb/call/statistic" % server
scb_credentials = "%s/SmiddleSmartCallback/scb/credentials" % server

# Smart_Proxy
proxy_list = "%s/SmiddleSIPProxy/ssp/phone/list" % server
proxy_prefix = '%s/SmiddleSIPProxy/ssp/phone/prefix' % server
proxy_logs = "%s/SmiddleSIPProxy/ssp/logs" % server
proxy_manifest = "%s/SmiddleSIPProxy/ssp/manifest" % server
proxy_licenses = "%s/SmiddleSIPProxy/ssp/licenses" % server
proxy_settings = "%s/SmiddleSIPProxy/ssp/settings" % server

# QOS
criteria_group = "%s/SmiddleQualityService/qos/template/criteria_group" % server
criteria = "%s/SmiddleQualityService/qos/template/criteria" % server
delete_criteria_group = "%s/SmiddleQualityService/qos/template//delete_criteria_group" % server
edit_template = "%s/SmiddleQualityService/qos/template/edit_template"%server

# QOS
questioner = "%s/SmiddleQualityService_CA/qos/ca/questioner" % server
filter = "%s/SmiddleQualityService_CA/qos/ca/questioner/filter" % server
abonent = "%s/SmiddleQualityService_CA/qos/ca/questioner/filter/phone/import" % server
agent = "%s/SmiddleQualityService_CA/qos/ca/questioner/filter/agent" % server
