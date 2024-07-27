document.addEventListener('DOMContentLoaded', function () {
    // Select all elements with the class 'toast'
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
  
    // Initialize each toast element
    var toastList = toastElList.map(function (toastEl) {
      return new bootstrap.Toast(toastEl, {
        delay: 3000 // Set the auto-hide delay to 3 seconds
      });
    });
  
    // Show each toast
    toastList.forEach(toast => toast.show());
  });
  