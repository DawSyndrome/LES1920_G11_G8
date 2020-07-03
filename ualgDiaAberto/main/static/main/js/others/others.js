function removeA(arr) {
  var what, a = arguments, L = a.length, ax;
  while (L > 1 && arr.length) {
    what = a[--L];
    while ((ax= arr.indexOf(what)) !== -1) {
      arr.splice(ax, 1);
    }
  }
  return arr;
}

var row_list = [];

function subtract(element){

  var val = $(element).closest("#subscribe_div").find("input[name='subscribers_qtt']").val();
  var decrement = parseInt(val) - 1;

  if (element.title == 'subtrair inscrito') {

    if ( parseInt(val) > 0 ) {

      $(element).closest("#subscribe_div").find("input[name='subscribers_qtt']").attr('value', decrement.toString());

      if (row_list.includes(element.id) == true) {

        $("#choiced_sessions").find(`input[id="${element.id}"][name="subscribers_qtt"]`).attr('value', decrement.toString());

      }

    }

    if (decrement === 0) {

      if (row_list.includes(element.id) == true) {

        $(`tr[id="${element.id}"]`).remove();

        removeA(row_list, element.id);

      }

    }

  } else if (element.title == 'subtrair') {

    if ( parseInt(val) > 0 ) {

      $("#choiced_sessions").find(`input[id="${element.id}"][name="subscribers_qtt"]`).attr('value', decrement.toString());
      $(`input[id="${element.id}"][title="main_s"]`).attr('value', decrement.toString());

    }

    if (decrement === 0) {

      if (row_list.includes(element.id) == true) {

        $(`tr[id="${element.id}"]`).remove();

        removeA(row_list, element.id);

      }

    }

  }

  var tbody = $("#choiced_sessions #sub_tbody");

  if (tbody.children().length == 0) {

    $('#sub_thead').remove();

    var no_choiced_sessions = document.getElementById('no_choiced_sessions');
    no_choiced_sessions.style.display = 'inline';

  }

}

function delRow(element) {
  removeA(row_list, element.id);
  $(`tr[id="${element.id}"]`).remove();

  var tbody = $("#choiced_sessions #sub_tbody");

  if (tbody.children().length == 0) {
    $('#sub_thead').remove();

    var no_choiced_sessions = document.getElementById('no_choiced_sessions');
    no_choiced_sessions.style.display = 'inline';

    $(`input[id="${element.id}"][title="main_s"]`).val(0);

  }

}

function add(element){
  var val = $(element).closest("#subscribe_div").find("input[name='subscribers_qtt']").val();
  var increment = parseInt(val) + 1;

  var test = $(element).closest("#subscribe_div").find("input[name='subscribers_qtt']").attr('value', increment.toString());

  var no_choiced_sessions = document.getElementById('no_choiced_sessions');
  no_choiced_sessions.style.display = 'none';

  if (element.title == 'somar') {
    $(`input[id="${element.id}"][title="main_s"]`).attr('value', increment.toString());
  }

  if (row_list.includes(element.id) == true) {

    $("#choiced_sessions").find(`input[id="${element.id}"][name="subscribers_qtt"]`).attr('value', increment.toString());

  } else {

    var activity_id = $(element).closest("#subscribe_div").find("input[name='activity_id'][type=hidden]").val();
    var session_id = $(element).closest("#subscribe_div").find("input[name='session_id'][type=hidden]").val();
    var schedule = $(element).closest("#subscribe_div").find("input[name='schedule'][type=hidden]").val();
    var activity = $(element).closest("#subscribe_div").find("input[name='activity'][type=hidden]").val();
    var place = $(element).closest("#subscribe_div").find("input[name='place'][type=hidden]").val();
    var campus = $(element).closest("#subscribe_div").find("input[name='campus'][type=hidden]").val();

    let new_header = `
      <thead id="sub_thead" class="bg-primary-600">
        <tr>
          <th>Horário</th>
          <th>Inscritos</th>
          <th>Atividade</th>
          <th>Espaço</th>
          <th>Campus</th>
          <th>Ações</th>
        </tr>
      </thead>
    `;

    let new_row = `
      <tbody id="sub_tbody">
        <tr id="${element.id}">
          <input type="hidden" name="sub_activity_id" value="${activity_id}">
          <input type="hidden" name="sub_session_id" value="${session_id}">
          <td>${schedule}</td>
          <td>
            <div id="subscribe_div">
              <div>
                <input title="subtrair" type="button" id="${element.id}" name="subs_less_btn" value="-" onclick="subtract(this)">
              </div>
              <div>
                <input id="${element.id}" type="text" name="subscribers_qtt" value="${increment.toString()}" oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');">
              </div>
              <div>
                <input title="somar" type="button" id="${element.id}" name="subs_plus_btn" value="+" onclick="add(this)">
              </div>
            </div>
          </td>
          <td>${activity}</td>
          <td>${place}</td>
          <td>${campus}</td>
          <td>
            <i id="${element.id}" onclick="delRow(this)" title="delete" class="far fa-trash-alt"></i>
          </td>
        </tr>
      <tbody>
    `;

    var tbody = $("#choiced_sessions #sub_tbody");

    if (tbody.children().length == 0) {
      $('#choiced_sessions').append(new_header);
    }

    $('#choiced_sessions').append(new_row);

    row_list.push(element.id);

  }

}

$('a[id=more_filters]').on('click', function(){
  var moreFilter = document.getElementById('more_filters');
  moreFilter.style.display = 'none';
  var lessFilter = document.getElementById('less_filters');
  lessFilter.style.display = 'inline';
  var filters = document.getElementById('filters');
  filters.style.display = 'inline';
});

$('a[id=less_filters]').on('click', function(){
  var moreFilter = document.getElementById('more_filters');
  moreFilter.style.display = 'inline';
  var lessFilter = document.getElementById('less_filters');
  lessFilter.style.display = 'none';
  var filters = document.getElementById('filters');
  filters.style.display = 'none';
});

function subtractVacancies(e){
  var val = $(e).closest("#minus_vacancies").find("input[name='vacancies_qtt']").val();
  if ( parseInt(val) > 0 ) {
    $(e).closest("#minus_vacancies").find("input[name='vacancies_qtt']").attr('value', parseInt(val) - 1);
  }
};

function addVacancies(e){
  var val = $(e).closest("#minus_vacancies").find("input[name='vacancies_qtt']").val();
  $(e).closest("#minus_vacancies").find("input[name='vacancies_qtt']").attr('value', parseInt(val) + 1);
};