<%@ taglib prefix="layout" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page session="false" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width", initial-scale="1"> <!--initial-scale의 내용은 일반적인 비율로, content의 내용은 장치의 너비와 일치하도록, viewport는 접속한 디바이스의 크기에 맞게 -->
		<title>MotionDetection</title>
		<link rel="stylesheet" href="resources/static/css/bootstrap.css"> <!--bootstrap.css를 이용해서 스타일을 꾸미겠다는-->
		<link rel="stylesheet" href="resources/static/css/MotionDetection.css">
	<style type="text/css">
			.jumbotron {
				background-image: url('images/jumbotronBackground.jpg');
				background-size: cover;
				text-shadow: black 0.2em 0.2em 0.2em;
				color: white;
			}
		</style>
</head>
<body>
		<footer style="background-color: #000000; color: #ffffff">
			<div class="container">
				<br>
				<div class="row"> <!--row는 기본적으로 12칸으로 나뉠 수 있게 되있다.-->
					<div class="col-sm-3" style="text-align: center;"><h5>Copyright &copy; 2020</h5><h5>KwangWoon Park</div>
					<div class="col-sm-4"><h4>회사 소개</h4><p>한국항공대학교 소프트웨어학과</p></div>
					<div class="col-sm-2"><h4 style="text-align: center;">Navigation</h4>
						<div class="list-group">
							<a href="index" class="list-group-item">Home</a>
							<a href="camera" class="list-group-item">Cam video</a>
							<a href="fireNews" class="list-group-item">화재 기사</a>
						</div>
					</div>
					<div class="col-sm-2"><h4 style="text-align: center;">SNS</h4>
						<div class="list-group">
							<a href="https://www.facebook.com/kwangwoon.park.12/" class="list-group-item">Facebook</a>
							<a href="https://www.youtube.com/channel/UCAXCDlfNa4mirYpHTOFbwYA?view_as=subscriber" class="list-group-item">YouTube</a>
						</div>
					</div>
				</div>
			</div>			
		</footer>
		<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
		<script src="js/bootstrap.js"></script>
	</body>
</html>