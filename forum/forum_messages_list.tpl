<h1>Forum message List </h1>
%for themes, messages in rows.iteritems():
    <h1>{{themes}}</h1>
    %for message in messages:
        <table border="1" id="forum_table">
        %subject = message['subject']
        %text = message['message']
        <tr>
        <th>{{subject}}</th>
        </tr>
        <tr>
        <td>{{text}}</td>
        </tr>
        </table>
        <p></p>
%end

