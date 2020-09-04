<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>    
    
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/button.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/table.css">
<link rel="stylesheet" href="${pageContext.request.contextPath}/resources/css/main.css">
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<title>Insert title here</title>
</head>
<body>

<div id="output">
    <section>
    
  
<h2>로그인 폼</h2>
<form id="fomr1" name="form1"  action="login.do" method="post" >
    <table border="1">
       <tr>
          <td colspan="2">
          <span style="color:red">${msg}</span>
          </td>
       </tr>
    
       <tr>
          <td>ID</td>
          <td><input type="text" id="id" name="userid" required="required"></td>
       </tr>
       <tr>
          <td>PW</td>
          <td><input type="text" id="pw" name="userpwd" 
                  required="required"></td>
       </tr>
       <tr align="center">
          <td colspan="2">
             <input type="submit" value="로그인" >
             <input type="reset" value="취소">
          </td>
       </tr>
       <tr>
          <td colspan="2">
             <a href="#"> User 등록   </a>
          </td>
       </tr>
    </table>
</form>  
    
    </section>
</div>

</body>
</html>