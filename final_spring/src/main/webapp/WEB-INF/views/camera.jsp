<%@ page session="false"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!--점보트론은 부트스트랩에서 홈페이지를 소개하는 메인 전광판을 의미-->
<style type="text/css">
blockquote {
	background: #f9f9f9f9;
	border-left: 10px solid #cccccc;
	margin: 1.5em 10px;
	padding: 0.5em 10px;
	quotes: "\201C" "\201D" "\2020" "\2021";
}

blockquote:before {
	color: #cccccc;
	content: open-quote;
	font-size: 3em;
	line-height: 0.1em;
	margin-left: 0.25em;
	vertical-align: -0.4em;
}

blockquote:after {
	color: #cccccc;
	content: close-quote;
	font-size: 3em;
	line-height: 0.1em;
	margin-left: 0.25em;
	vertical-align: -0.4em;
}
</style>
<%@ include file="/WEB-INF/views/top.jsp"%>
<div class="container">
	<!--table을 담을 수 있는 container-->
	<div class="row">
		<div class=col-xs-12">
			<div class="panel panel-primary">
				<div class="panel-heading">
					<h3 class="panel-title">
						<span class="glyphicon glyphicon-film"></span> &nbsp;&nbsp;MD CAM
					</h3>
				</div>
				<div class="panel-body">
					<div class="media">
						<div class="media-left">
							<a href="#"> <img class="media-object"
								src="resources/static/images/cam.jpg" alt="CAM 이미지">
							</a>
						</div>
						<div class="media-body">
							<h4 class="media-heading">Video</h4>
							<br> Motion Detection Cam의 영상입니다.
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<ul class="list-group">
							<a href="#" class="list-group-item active">CAM-01</a>
							<div class="embed-responsive embed-responsive-16by9">
								<iframe class="embed-responsive-item"
									src="https://www.youtube.com/embed/fOdpLTO7qrE"> </iframe>
							</div>
							<a href="#" class="list-group-item">CAM-02</a>
							<a href="#" class="list-group-item">CAM-03</a>
						</ul>
					</div>
				</div>
				<!-- <table class="table">
							<thead>
								<tr>
									<th>영상 번호</th>
									<th>영상명</th>
									<th>영상 날짜</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td>1</td>
									<td>CAM-01</td>
									<td>2020-09-15</td>
								</tr>
								
								<tr>
									<td>2</td>
									<td>CAM-02</td>
									<td>2020-09-16</td>
								</tr>
								<tr>
									<td>3</td>
									<td>CAM-03</td>
									<td>2020-09-17</td>
								</tr>
							</tbody>
						</table> -->
			</div>
		</div>
	</div>
</div>
<%@ include file="/WEB-INF/views/footer.jsp"%>