$(document).ready( function () {
            $.ajax({
              dataType: "json",
              url: "http://127.0.0.1:8000/user/list_all/",
              success: function (result) {
                  $('#displayTable').DataTable({
                      "bProcessing" : true,
                      "data": result,
                      "columns":[
                          {"data" : "age"},
                          {"data" : "wrk_cls_val"},
                          {"data" : "fnl_wgt"},
                          {"data" : "edu_val"},
                          {"data" : "edu_num"},
                          {"data" : "mar_status_val"},
                          {"data" : "occupation_val"},
                          {"data" : "relation_val"},
                          {"data" : "race_val"},
                          {"data" : "gender_val"},
                          {"data" : "cap_gain"},
                          {"data" : "cap_loss"},
                          {"data" : "hrs_per_week"},
                          {"data" : "country_val"},
                          {"data" : "class_grp_val"},
                      ]
                });
              }
            });
        } );