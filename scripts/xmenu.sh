#!/bin/sh

# Generates colors-xmenu.h configuration file

. $HOME/.cache/wal/colors.sh

cat <<CONF
static struct Config config = {
		/* font */
  .font = "HackNerdFont:size=9,FontAwesome:size=9,FontAwesomeBrands:size=11",
	/* colors */
	.background_color = "${background}",
	.foreground_color = "${foreground}",
	.selbackground_color = "${cursor}",
	.selforeground_color = "${color0}",
	.separator_color = "${color1}",
	.border_color = "${color2}",
	/* sizes in pixels */
	.width_pixels = 130,        /* minimum width of a menu */
	.height_pixels = 25,        /* height of a single menu item */
	.border_pixels = 1,         /* menu border */
	.separator_pixels = 3,      /* space around separator */
	.gap_pixels = 2,            /* gap between menus */
	/*
	 * The variables below cannot be set by X resources.
	 * Their values must be less than .height_pixels.
	 */
	/* geometry of the right-pointing isoceles triangle for submenus */
	.triangle_width = 4,
	.triangle_height = 7,
	/* the icon size is equal to .height_pixels - .iconpadding * 2 */
	.iconpadding = 2,
	/* area around the icon, the triangle and the separator */
	.horzpadding = 10,
};
CONF
