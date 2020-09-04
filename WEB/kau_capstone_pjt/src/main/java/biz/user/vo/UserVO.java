package biz.user.vo;

import java.io.Serializable;

public class UserVO implements Serializable{ 
	String name;
	String user_id;
	String pw;
	
	public UserVO() {}
	
	public UserVO(String name, String user_id, String pw) {
		super();
		this.name = name;
		this.user_id = user_id;
		this.pw = pw;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getUser_id() {
		return user_id;
	}

	public void setUser_id(String user_id) {
		this.user_id = user_id;
	}

	public String getPw() {
		return pw;
	}

	public void setPw(String pw) {
		this.pw = pw;
	}

	@Override
	public String toString() {
		return "UserVO [name=" + name + ", user_id=" + user_id + ", pw=" + pw + "]";
	}
	
}
	

