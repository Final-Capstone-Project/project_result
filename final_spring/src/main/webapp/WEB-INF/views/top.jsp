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
	<nav class="navbar navbar-default">
			<div class="container-fruid">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
						<span class="sr-only"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="/">Motion Detection</a>
				</div>
				<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					<ul class="nav navbar-nav">
						<li class="dropdown">
							<a href="/fire" class="dropdown-toggle" data-toggle="dropdown" role="button"
								aria-haspopup="true" aria-expanded="false">화재<span class="caret"></span></a>
							<ul class="dropdown-menu">
								<li><a href="https://www.nfa.go.kr/nfa/news/firenews/disasterNews/">화재 기사</a></li>
								<li><a href="/fireStatus">화재 현황</a></li>
							</ul>
						</li>
					</ul>
					<form class="navbar-form navbar-left">
						<div class="form-group">
							<input type="text" class="form-control" placeholder="내용을 입력하세요.">
						</div>
						<button type="submit" class="btn btn-default">Search</button> <!--form태그에 입력한 내용이 서버로 전달-->
					</form> <!--form태그는 어떠한 서버로 요청을 전달할 수 있게 해주는 태그다.-->
					<ul class="nav navbar-nav navbar-right">
						<li class="dropdown">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
								aria-haspopup="true" aria-expanded="false">Sign in<span class="caret"></span></a>
							<ul class="dropdown-menu">
								<li><a href="/loginForm">로그인</a></li>
								<li><a href="/registerForm">회원가입</a></li>
							</ul>
						</li>					
					</ul>
				</div>
			</div>
		</nav>
</body>
</html>