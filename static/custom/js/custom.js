// this module is used for login and register functionality
var productModule = {
    buttonAdd: function () {
        var form = new FormData()
        form.append('barcode', $('#id_barcode').val())
        form.append('product_name', $('#id_product_name').val())
        form.append('product_description', $('#id_product_description').val())
        form.append('product_brand', $('#id_product_brand').val())
        form.append('product_score', $('#id_product_score').val())
        form.append('product_image', $('#id_product_image')[0].files[0])
        var url = '/add/';
        var data = form;
        var type = 'POST';
        NetworkModule.multiUploadData(url, type, data, function (response) {
            if (response === 'success') {
                swal('Success', 'Product has been Added', 'success');
                window.location.href = '/'
            } else {
                swal('Error', 'Network Error', 'error');
            }
        })
    },
    signIn: function () {
        var url = '/login/';
        var data = $('#userForm').serialize();
        var type = 'POST';
        NetworkModule.getData(url, type, data, function (response) {
            if (response != 'success') {
                swal('Error', 'Incorrect Username and Password', 'error')
            } else {
                window.location.href = '/'
            }
        })
    },
    delete: function (id) {
        swal({
            title: "Do you want to delete the product?",
            icon: "warning",
            showCancelButton: true,
            //dangerMode: true, //set this in case the focus should be on cancel button
            buttons: {
                cancel: true,
                confirm: true,
            },
        }).then(isConfirmed => {
                if (isConfirmed) {
                    var url = 'delete/' + id + '/';
                    var data = {};
                    var type = 'DELETE';
                    NetworkModule.getData(url, type, data, function (response) {
                        if (response) {
                            $('.productTable').html(response)
                            swal('sucess','Product Deleted!!','success');
                        } else {
                            swal('error', 'Network Error', 'error')
                        }

                    })
                } else {
                    swal('Success','Item Not Deleted!!','success')
                }
            }
        );
    },
    update: function (id) {
        var form = new FormData()
        form.append('barcode', $('#id_barcode').val())
        form.append('product_name', $('#id_product_name').val())
        form.append('product_description', $('#id_product_description').val())
        form.append('product_brand', $('#id_product_brand').val())
        form.append('product_score', $('#id_product_score').val())
        form.append('product_image', $('#id_product_image')[0].files[0])
        var url = 'update/' + id + '/';
        var data = form;
        var type = 'POST';
        NetworkModule.multiUploadData(url, type, data, function (response) {
            if (response === 'success') {
                swal({
                    title: "Product has been Updated",
                    icon: "success",
                    showCancelButton: false,
                    //dangerMode: true, //set this in case the focus should be on cancel button
                    buttons: {
                        cancel: false,
                        confirm: true,
                    },
                }).then(isConfirmed => {
                    if (isConfirmed) {
                        window.location.href = '/'
                    }
                });

            } else {
                swal('Error', 'Network Error', 'error');
            }
        })
    },

    init: function () {
        this.buttonAdd();
        this.signIn();
        this.delete(id);
    }

};