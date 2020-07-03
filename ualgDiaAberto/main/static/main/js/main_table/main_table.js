/* Formatting function for row details - modify as you need */
function format ( d ) {
  // `d` is the original data object for the row

  return `
    <tr id="sub_details" class="detail">
      <td colspan="6">
        <div class="detail-container">
          <div class="content">
            <div style="font-size: 15px;">
              <p>${d.desc}</p>
              <p><strong>Responsável:</strong> ${d.resp}</p>
              <div class="b-table">
                <div class="table-wrapper">
                  <table id="sub_table" class="table has-mobile-cards">
                    <thead>
                      <tr>
                        <th class="">
                          <div class="th-wrap">
                            Hora <span class="icon is-small" style="display: none;"><i class="mdi mdi-arrow-up"></i></span>
                          </div>
                        </th>
                        <th class="">
                          <div class="th-wrap">
                            Duração <span class="icon is-small" style="display: none;"><i class="mdi mdi-arrow-up"></i></span>
                          </div>
                        </th>
                        <th class="">
                          <div class="th-wrap">
                            Vagas <span class="icon is-small" style="display: none;"><i class="mdi mdi-arrow-up"></i></span>
                          </div>
                        </th>
                        <th class="">
                          <div class="th-wrap">
                            Espaço <span class="icon is-small" style="display: none;"><i class="mdi mdi-arrow-up"></i></span>
                          </div>
                        </th>
                        <th class="">
                          <div class="th-wrap" style="text-align: center;">
                            Inscrever <span class="icon is-small" style="display: none;"><i class="mdi mdi-arrow-up"></i></span>
                          </div>
                        </th>
                      </tr>
                    </thead>

                    <tbody>
                      <tr>
                        <td data-label="Hora"> ${d.hour} </td>
                        <td data-label="Duração"> ${d.duration} min</td>
                        <td data-label="Vagas"> ${d.vacancies} </td>
                        <td data-label="Espaço"> ${d.place} </td>

                        <td data-label="Inscrever">
                          <div id="subscribe_div">
                            <input type="hidden" name="activity_id" value="${d.activity_id}">
                            <input type="hidden" name="session_id" value="${d.session_id}">
                            <input type="hidden" name="schedule" value="${d.schedule}">
                            <input type="hidden" name="activity" value="${d.name}">
                            <input type="hidden" name="place" value="${d.place}">
                            <input type="hidden" name="campus" value="${d.campus}">

                            <div>
                              <input title="subtrair inscrito" type="button" id="${d.name}" name="subs_less_btn" value="-" onclick="subtract(this)">
                            </div>
                            <div>
                              <input title="main_s" id="${d.name}" type="text" name="subscribers_qtt" value="0" oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');">
                            </div>
                            <div>
                              <input title="somar inscrito" type="button" id="${d.name}" name="subs_plus_btn" value="+" onclick="add(this)">
                            </div>
                          </div>
                        </td>

                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </td>
    </tr>
  `;
}

var table;
 
$(document).ready(function() {
  table = $('#main_table').DataTable({
    sDom: 'lrtip',
    "searching": true,
    bInfo: false,
    "columnDefs": [
      {
        "targets": [6],
        "visible": false,
        "searchable": true
      },
      {
        "targets": [7],
        "visible": false,
        "searchable": true
      }
    ],
    responsive: true,
    lengthChange: false,
    pageLength: 7,
    "ajax": '/static/main/js/data/main_table.json',
    "columns": [
      {
        "className": 'details-control',
        "orderable": false,
        "data": null,
        "defaultContent": ''
      },

      {"data": "name"},
      {"data": "kind"},
      {"data": "campus"},
      {"data": "eo"},
      {"data": "dep"},
      {"data": "hour"},
      {"data": "end_hour"}
    ],
    "order": [[1, 'asc']]
  });

  // #search is a <input type="text"> element
  $('#search').on('keyup', function () {
    console.log('A new value was typed. The value is: ' + this.value);
    table.columns(1).search(this.value).draw();
  });

  $('#select_activity_kind').on('change', function () {
    table.columns(2).search(this.value).draw();
  });

  $('#select_campus').on('change', function () {
    table.columns(3).search(this.value).draw();
  });

  $('#select_eo').on('change', function () {
    table.columns(4).search(this.value).draw();
  });
     
  // Add event listener for opening and closing details
  $('#main_table tbody').on('click', 'td.details-control', function () {
    var tr = $(this).closest('tr');
    var row = table.row( tr );

    if ( row.child.isShown() ) {
      // This row is already open - close it
      row.child.hide();
      tr.removeClass('shown');
    } else {
      // Open this row
      row.child( format(row.data()) ).show();
      tr.addClass('shown');
    }

  });

});

// ########################################################################################

function showpickers1(a,b){
  if(showpicker){
    $('.tpicker').hide();
    showpicker=0;

    var timepkr_from = document.getElementById('timepkr_from');
    var from = timepkr_from.value;

    if (from != '') {

      table.columns(6).search(from).draw();

    }

  }else{
    elid = a;
    picker_type = b;
    var x = $("#"+elid).offset();
    $('.tpicker').show();
    var kk = $("#"+elid).outerHeight();
    $('.tpicker').offset({ top: x.top+kk, left: x.left});
    showpicker=1;
  }
}

function showpickers2(a,b){
  if(showpicker){
    $('.tpicker').hide();
    showpicker=0;

    var timepkr_to = document.getElementById('timepkr_to');
    var to = timepkr_to.value;

    if (to != '') {

      table.columns(7).search(to).draw();

    }

  }else{
    elid = a;
    picker_type = b;
    var x = $("#"+elid).offset();
    $('.tpicker').show();
    var kk = $("#"+elid).outerHeight();
    $('.tpicker').offset({ top: x.top+kk, left: x.left});
    showpicker=1;
  }
}

// ########################################################################################
