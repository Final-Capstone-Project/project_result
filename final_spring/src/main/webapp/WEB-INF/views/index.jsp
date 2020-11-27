<%@ page session="false"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<style type="text/css">
.jumbotron {
	background-image:
		url('C:/Users/qkrrh/eclipse-workspace/final_spring/src/main/webapp/images/jumbotronBackground.jpg');
	background-size: cover;
	text-shadow: black 0.2em 0.2em 0.2em;
	color: white;
}
</style>
<%@ include file="/WEB-INF/views/top.jsp"%>
<div class="container">
	<div class="jumbotron">
		<h1 class="text-center">Motion Detection Camera</h1>
		<!--가장 큰 글씨를 나타낼 때-->
		<p class="text-center">Motion Detection Camera는 화재 및 방범을 위한 cctv를
			제공합니다.</p>
		<!--한 문장을 표시할 때-->
		<p class="text-center">
			<a class="btn btn-primary btn-lg" href="camera" role="button">CCTV영상
				확인</a>
		</p>
		<!--a태그는 링크로 이동할 수 있도록 해주는 태그-->
	</div>
	<div class="row">
		<div class="col-md-4">
			<h4>특징</h4>
			<p>Motion Detection Camera의 특징.</p>
			<p>
				<a class="btn btn-default" data-target="#modal" data-toggle="modal">자세히
					알아보기</a>
			</p>
		</div>
		<div class="col-md-4">
			<h4>화재 현황 보기</h4>
			<p>연간 발생한 화재 현황을 확인할 수 있습니다.</p>
			<p>
				<a class="btn btn-default" href="fireStatus">현황 한 눈에 보기</a>
			</p>
		</div>
		<div class="col-md-4">
			<h4>고객 센터</h4>
			<p>문의사항이 있으신 분은 아래 번호로 연락바랍니다.</p>
			<p>
				<a class="btn btn-default" href="#">☎ 070-1029-3847</a>
			</p>
		</div>
	</div>
	<hr>
	<!--한 줄이 그어진다.-->
	<div class="panel panel-primary">
		<div class="panel-heading">
			<h3 class="panel-title">
				<span class="glyphicon glyphicon-plus"></span> &nbsp;&nbsp;최신 소식
			</h3>
		</div>
		<div class="panel-body">
			<div class="media">
				<div class="media-left">
					<a href="camera"><img class="media-object"
						src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\cam.jpg"
						alt="cam 이미지"></a>
					<!--alt는 웹사이트를 눈으로 보지 못하는 사람들을 위해 해당 이미지가 어떤 이미지인지 띄어주는 것-->
				</div>
				<div class="media-body">
					<h4 class="media-heading">
						<a href="camera">&nbsp;최근 영상 내역</a>&nbsp;<span class="badge">New</span>
					</h4>
					&nbsp;최근 일주일간의 영상 기록을 확인하실 수 있습니다.
				</div>
			</div>
			<hr>
			<div class="media">
				<div class="media-left">
					<a href="fireNews"><img class="media-object"
						src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\fire.jpg"
						alt="fire 이미지"></a>
					<!--alt는 웹사이트를 눈으로 보지 못하는 사람들을 위해 해당 이미지가 어떤 이미지인지 띄어주는 것-->
				</div>
				<div class="media-body">
					<h4 class="media-heading">
						<a href="fireNews">&nbsp;최근 화재 소식</a>&nbsp;<span class="badge">New</span>
					</h4>
					&nbsp;최근에 발생한 화재 기사를 확인 할 수 있습니다.
				</div>
			</div>
		</div>
	</div>
	<div class="row">
		<div class="modal" id="modal" tabindex="-1">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						Motion Detection Camera의 특징
						<button class="close" data-dismiss="modal">&times;</button>
					</div>
					<div class="modal-body" style="text-align: center;">
						저희 서비스의 특징은 바로 화재 및 침입 감지 시 영상과 알림을 제공합니다.<br> <br>
						<!--img src="#" id="imagepreview" style="width: 256px; height: 256px;"-->
					</div>
				</div>
			</div>
		</div>
	</div>
	<%@ include file="/WEB-INF/views/footer.jsp"%>