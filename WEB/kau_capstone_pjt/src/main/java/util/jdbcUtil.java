package util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class jdbcUtil { 
	
	static String driver = "oracle.jdbc.driver.OracleDriver";
	static String url = "jdbc:oracle:thin:@localhost:1521:xe";
	static String user = "hr";
	static String pw = "hr";
	
	public static Connection getConnection() {
		//connection 만들어서 리턴 
		Connection con = null;
		
		try {
			Class.forName(driver);
			con = DriverManager.getConnection(url, user, pw);
			
		} catch (ClassNotFoundException e) {
			System.out.println("driver를 확인하세요");
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		return con;
	}
	
	public static void close(ResultSet rs, Statement st, Connection con) {
		//connection 반납해야될 자원 관리 
		try {
			if(rs != null) rs.close();
			if(st != null) st.close();
			if(con != null) con.close();
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
}
