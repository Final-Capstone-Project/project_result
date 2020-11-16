<%@ page session="false"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<style type="text/css">
.statusTitle {
	text-align: center;
	color: darkgreen;
}

.imgcontainer .image {
	background-color: white;
	width: 33.33%;
	float: left;
}

.imgcontainer img {
	background-color: white;
	width: calc(100% - ( 20px * 2));
	margin: 20px;
}
</style>
<%@ include file="/WEB-INF/views/top.jsp"%>
<br>
<h2 class="statusTitle" text-align="center">
	<b>서울시 세부 화재 현황</b>
</h2>
<div class="container">
	<script>
		function img_change(f) {
			var chimg = '<img src="' + $(f).find('option:selected').data('src')
					+ '">';
			$('#change_img').html(chimg);
		}
	</script>
	<div class="text-center">
		<form name="search">
			<select id="fireStatus" onchange="img_change(this);"
				class="btn btn-light dropdown-toggle">
				<option value="">항목 선택</option>
				<option value="year"
					data-src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\year.png">연도별</option>
				<option value="city"
					data-src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\city.png">구별</option>
				<option value="casualty"
					data-src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\casualty.png">사상자별</option>
				<option value="place"
					data-src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\place.png">장소별</option>
				<option value="cause"
					data-src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\cause.png">원인별</option>
				<option value="carelessness"
					data-src="C:\Users\qkrrh\eclipse-workspace\final_spring\src\main\webapp\images\carelessness.png">부주의
					유형별</option>
			</select>
			<div id="change_img" align="center"></div>
		</form>
	</div>
</div>
<br>
<%@ include file="/WEB-INF/views/footer.jsp"%>