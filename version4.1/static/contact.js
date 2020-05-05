$(document).ready(function () {

    $("#submit_comment").click(function () {
        _validateForm();
    });

    function _validateForm() {
        var ID = $("#ID").val();
        var comment = $("#comment").val();

        var iddd =_idIsValid(ID)
        console.log('iddd ',ID,  iddd);
        
        var com = _commentIsValid(comment)
        console.log('comment ',comment, com, comment.match(/\S+/g).length);

        if (!_idIsValid(ID)){
            alert(" WRONG Email address ")
        }
        else if (!_commentIsValid(comment)){
            alert(" Comment should more than 5 words! ")
        }

        else {
            _write(ID, comment)
        }


    }


    function _write(ID, comment){
        var data = {
            ID: ID,
            comment: comment
        };

        console.log(data);
        $.ajax({
            type: "POST",
            url: "/contact",
            data: data,
            dataType: 'json'
        }).always(function (xhr) {
            alert(" Tks, I recieved your comment! ")
            location.reload();

        });
    }

    function _idIsValid(ID) {
        return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(ID)
    }

    function _commentIsValid(comment) {
        return comment.match(/\S+/g).length > 4
    }

})