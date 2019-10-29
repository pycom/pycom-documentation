/*
* Smooth scroll to anchor link
*/


$(document).ready(function(){
    $( 'a[href^="#"]' ).on( 'click', function( e ) {

        if ( this.hash !== '' ) {
            e.preventDefault();

            var hash = this.hash;
            var nav = $( '.navbar' ).outerHeight();
            var targetOffset = $( hash ).offset().top - nav;

            $( 'html, body' ).animate( {
                scrollTop: targetOffset
            }, 1100, function() {
                //window.location.hash = hash;
            } );
        }
    } );
} );
