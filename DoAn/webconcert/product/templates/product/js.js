        var loai="Food";
        function getLoai(value){
          loai=value
        }
        function isNumeric(num){
          return !isNaN(num)
        }
        function send() {

         var ten= document.getElementById('ten').value;
         var soluong= document.getElementById('soluong').value;
         var email= document.getElementById('email').value;
         if(email==='' || soluong ===' '|| ten===''){
          alert("Thông tin đăng ký chưa đầy đủ");
          return;
        }
        if(isNumeric(soluong)==false){
         alert("Thông tin Về số lượng chưa đúng định dạng");
         return;
       }
       var bd="Hi " +ten+" đơn Hàng đã đăng kí thành công. ";
       bd+="Bạn đã đăng kí "+ soluong+" bé "+loai;

       Email.send({
        Host: "smtp.gmail.com",
        Username: "hatran192.org@gmail.com",
        Password: "Khanhha192",
        SecureToken: "Generate token here",
        From: "hatran192.org@gmail.com",
        To: email,

        Subject: "Xác nhận đơn hàng: Pandora's Concept ",
        Body: bd
      }).then(function(response){

       if (response == 'OK') {
         alert("Tụi tui đã gửi mail xác nhận rồi nha, vui lòng check mail");
       } else {
         alert("Vui lòng nhập đúng định dạng email");
       }
     });

    }