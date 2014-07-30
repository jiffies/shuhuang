$(function(){
	var Book = Backbone.Model.extend({
		defaults: function(){
			return {
				title:"new book",
				author:"none",
				introduction:""
			};
		}
	});

	var BookList = Backbone.Collection.extend({
		url:'/books',
		model:Book
	});

	var Books=new BookList;
	
	var BookView = Backbone.View.extend({
		tagName: "li",
		template:_.template($("#item-template").html()),
		initialize:function(){
			this.listenTo(this.model,'change',this.render);
			this.listenTo(this.model,'destroy',this.remove);
		},
		render: function(){
			this.$el.html(this.template(this.model.toJSON()));
			return this;
		},
	});
	var AppView = Backbone.View.extend({
		el:$("#bookapp"),
		clitemplate:_.template($("#ctl-template").html()),
		//events: {
			//"click #next":"nextBook",
			//"click #prev":"prevBook",
		//},
		initialize:function(){
			this.listenTo(Books,'add',this.addOne);
			this.listenTo(Books,'reset',this.addAll);
			Books.fetch();
		},
		addOne:function(book){
			var view = new BookView({model:book});
			this.$("#book").append(view.render().el);
		},
		addAll:function(){
		Books.each(this.addOne,this);
		},

	});
	var app=new AppView;

});
