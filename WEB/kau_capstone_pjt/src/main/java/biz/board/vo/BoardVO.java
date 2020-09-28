package biz.board.vo;

public class BoardVO {
	int board_id;  // 글번호
	String title;
	String content;
	String writer;
	
	public BoardVO() {
		
	}
	
	public BoardVO(int board_id, String title, String content, String writer) {
		super();
		this.board_id = board_id;
		this.title = title;
		this.content = content;
		this.writer = writer;
	}

	public int getBoard_id() {
		return board_id;
	}

	public void setBoard_id(int board_id) {
		this.board_id = board_id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public String getWriter() {
		return writer;
	}

	public void setWriter(String writer) {
		this.writer = writer;
	}
	
	
}
