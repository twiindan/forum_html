%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>User List </p>
<table border="1">
<tr>
%for col in rows[0].keys():

    <th>{{col}}</th>

%end
</tr>
%for row in rows:
  <tr>
  %for col in row.values():
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>