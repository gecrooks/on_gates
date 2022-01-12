% FIXME
% Article option not working?
% Annote not working ?
% rename \titlemark?

\NeedsTeXFormat{LaTeX2e} 
\ProvidesClass{bespoke6} % Branch from bespoke5 April 2019


% ========== Process options ==========

\RequirePackage{etoolbox}	% Prefer over ifthen
\RequirePackage{ifdraft}

\newtoggle{formatArticle}
\newtoggle{formatBook} 
\newtoggle{formatNotes}	% For book preview notes

\newtoggle{pagebackrefFlag} 
\newtoggle{annotateFlag}
\newtoggle{stretchFlag}
\newtoggle{bookHeader}
\newtoggle{monochrome}
\newtoggle{macros}\toggletrue{macros}

\toggletrue{formatArticle}

\DeclareOption{book}{\toggletrue{formatBook}\togglefalse{formatArticle}}
\DeclareOption{notes}{\toggletrue{formatNotes}\togglefalse{formatArticle}}
\DeclareOption{pagebackref}{\toggletrue{pagebackrefFlag}}
\DeclareOption{annotate}{\toggletrue{annotateFlag}}
\DeclareOption{monochrome}{\toggletrue{monochrome}}
\DeclareOption{nomacros}{\togglefalse{macros}}		% Prevent automatic loading of macro package


\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions\relax



% ========== Page Geometry ==========

% Book format. 
\iftoggle{formatBook}{
	\LoadClass[10pt]{article}	% May not need twoside option here if it's in geometry. t
	% woside article option + geometry package seem to generate many underfull vboxes for no obvious reason. 
	\RequirePackage[
			paperwidth=6in,paperheight=9in,
			textheight=7in, 
			textwidth=4.5in, 
%			footskip=27pt,  headsep=15pt, headheight=12pt,
			footskip=36pt,  	headsep=24pt, headheight=18pt, 
			centering,
			twoside=true
			]{geometry}
	\pdfpagewidth=6in
	\pdfpageheight=9in			
	
	
	% Last page of a book should be completely blank.
	% Even number of pages
	\AtEndDocument{\clearpage\thispagestyle{empty}~\ifodd\value{page}\clearpage\thispagestyle{empty}~\fi}	
	\toggletrue{stretchFlag}	
	\toggletrue{bookHeader}	
}


\iftoggle{formatNotes}{
	\LoadClass[10pt]{article}
	\RequirePackage[paperwidth=8.5in,paperheight=11in, textheight=9.5in, textwidth=5in, %
				top=2.5cm, bottom=2.5cm,
				%footskip=36pt,  	headsep=24pt, headheight=18pt, 
				centering]{geometry}
	\pdfpagewidth=8.5in
	\pdfpageheight=11in
	\toggletrue{stretchFlag}	
	\toggletrue{bookHeader}			
} 

 
\iftoggle{formatArticle}{
	% Article format
	\LoadClass[twocolumn,twoside,10pt,letterpage]{article}
	\setlength{\columnsep}{0.5cm}
	\RequirePackage[paperwidth=8.5in,paperheight=11in, right=1.75cm, left=1.75cm, %
		top=2cm, bottom=2cm, centering]{geometry}
}







% ========== FONTS ==========

% Trump Mediaeval font looks better with extra line spacing
%TODO: But do these actually get used anywhere?
\RequirePackage{setspace}
\iftoggle{stretchFlag}{	
	% Book
	\newcommand{\normalstretch}{\setstretch{1.05}}
	\newcommand{\tightstretch}{\setstretch{0.95}}	
	\normalstretch
} {
	% Article
	\newcommand{\normalstretch}{\setstretch{1.0}}
	\newcommand{\tightstretch}{\setstretch{0.9}}		% Test
	\normalstretch
}

\RequirePackage{fontspec}
\RequirePackage[OT1]{fontenc}

\RequirePackage{eulervm} 			% Must be before amssymb
\RequirePackage{amsthm,amsmath}
\RequirePackage{amssymb}

%\usepackage{tgpagella,qpxmath}
\usepackage{tgpagella}

\usepackage{microtype}

% Need bold font
%\setromanfont[Mapping=tex-text, Scale=0.95,AutoFakeSlant]{Trump Mediaeval LT Std}
% Diacritics=Decompose not supported for this font
% Hack:  accent \=a needed for Sankhya, not working with this font. Using  $\bar{\text{a}}$  instead.
% FIXME: ALSO Birkh\:{a}user broken

% TODO: Change scale to 0.95?

% Fix various accents that don't appear in this font.
%\DeclareTextAccent{\`}{EU1}{"0060}    %grave
\DeclareTextAccent{\'}{EU1}{180}   %acute
\DeclareTextAccent{\^}{EU1}{"02C6}   %circumflex
\DeclareTextAccent{\~}{EU1}{"02DC}   %tilde
\DeclareTextAccent{\"}{EU1}{168}   %dieresis
\DeclareTextAccent{\H}{EU1}{"02DD}    %hungarumlaut
\DeclareTextAccent{\r}{EU1}{"02DA}    %ring
\DeclareTextAccent{\v}{EU1}{"02C7}    %caron
\DeclareTextAccent{\u}{EU1}{"02D8}    %breve
\DeclareTextAccent{\=}{EU1}{175}   %macron
\DeclareTextAccent{\.}{EU1}{"02D9}    %dotaccent

% Hacks because font doesn't seem to support these accents
\renewcommand{\v}[1]{$\check{\text{#1}}$}
\renewcommand{\=}[1]{$\bar{\text{#1}}$}
\renewcommand{\:}[1]{$\ddot{\text{#1}}$}

% ACCENT TEST STRING
% \`{a}\'{a}\^{a}\~{a}\"{a}\H{a}\r{a}\v{a}\u{a}\={a}\.{a}

% French spacing uses the same space as used between words.
% English spacing uses an en-space (half an em-space).
%\frenchspacing


% ========== HyperRef setup ==========
\RequirePackage[usenames,dvipsnames]{xcolor}

% To DO : Sort?\ RequirePackage[square,comma, numbers, sort]{natbib} \RequirePackage[square,comma, numbers, sort&compress]{natbib}

\iftoggle{pagebackrefFlag}{

	% ==========  Citation and Bibliography format ==========
	% = Page back refs. =
	% Do not compress when  using pagebackref's
	\RequirePackage[square,comma, numbers]{natbib}
	\bibliographystyle{bespoke5}

	\RequirePackage[
			pagebackref, 
			breaklinks
			%unicode
			]{hyperref}	
	\hypersetup{
		colorlinks=true, 
		urlcolor= MidnightBlue, 
		linkcolor= MidnightBlue, 
		citecolor= MidnightBlue  
	}
	\renewcommand*{\backrefalt}[4]{%
	  \ifcase #1 %
	    No citations.% use \relax if you do not want the "No citations" message
	  \or
	(page #4).%
	  \else
	(pages #4).%
	  \fi%
	}	
} { 
	% ==========  Citation and Bibliography format ==========
	% = No Page back refs. =
	
	\RequirePackage[square,comma, numbers,compress]{natbib}
	\bibliographystyle{bespoke5}		
		
	\RequirePackage[breaklinks]{hyperref}	
	\hypersetup{colorlinks=true, urlcolor= MidnightBlue,
		linkcolor= MidnightBlue, citecolor= MidnightBlue}
} %FI

% FIXME, does this work?
\iftoggle{annotateFlag}{\newcommand{\bibAnnote}[2]{#2} } { \newcommand{\bibAnnote}[2]{}}





% ========== Headers & Footers ==========


\newcommand{\titlemark}{} 


\RequirePackage{fancyhdr}
% \iffloatpage macro doesn't seem to work. (I think it used to?)

\fancypagestyle{plain}{
	\renewcommand{\headrulewidth}{0pt}
	\renewcommand{\footrulewidth}{0pt}
	\fancyhead{}
	\fancyfoot{}
	
	\iftoggle{bookHeader} {
		\iffloatpage{
			\fancyhead[C]{}
			\fancyfoot[C]{\small \scshape \titlemark}
		} {
			\fancyhead[C]{\nouppercase{\scshape\leftmark}}	
			\fancyfoot[C]{\small \scshape \titlemark } 
		}	
		
		\fancyfoot[OR]{\small \thepage}
		\fancyfoot[EL]{\small \thepage}
	}{
		\fancyhead[C]{\small \scshape \titlemark }
		\fancyfoot[C]{\small \thepage}
	}
}

\fancypagestyle{chapter}{
	\renewcommand{\headrulewidth}{0pt}
	\renewcommand{\footrulewidth}{0pt}
	\fancyhead{}
	\fancyfoot{}
	
	\iftoggle{bookHeader} {
%		\fancyfoot[C]{\small \itshape \titlemark } 
		\fancyhead[C]{\small \scshape \titlemark}
		\fancyfoot[OR]{\small \thepage}
		\fancyfoot[EL]{\small \thepage}		
	} {
		\fancyhead[C]{\small \scshape \titlemark}
		\fancyfoot[C]{\small \thepage}
	}
}
\pagestyle{plain}


% =========== Title ==========
\RequirePackage{environ}

\NewEnviron{Abstract}{\xdef\bespoke@abstract{\BODY}}
\newcommand{\preprint}[1]{\gdef\bespoke@preprint{#1}}

\def\@maketitle{%
  \newpage  
  \null
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\LARGE \@title \par}%
    
    \@ifundefined{bespoke@preprint} {} {
      \vskip 1.5em%
    {\normalsize\bespoke@preprint\par}%
    }
    
    \vskip 1.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
	
    \vskip 1em%
    {\large \@date}%
   \vskip 1em%
	 \@ifundefined{bespoke@abstract}{} {
	  {\large \bfseries \vspace{-8pt}}\par
	 	\begin{quote}\noindent \bespoke@abstract \end{quote}
		}
	
  \end{center}%
  \par
  \vskip 1.5em%


%\hypersetup{ 
%	pdfauthor={\@author}, 
%	pdftitle={\@title},
%	pdfpagemode=UseOutlines
%}

}
\makeatother

% Title colors
\usepackage{sectsty}

\iftoggle{monochrome}{
	\hypersetup{colorlinks=false}
	\def\titlecolor{Black}
	}{
	\def\titlecolor{BrickRed}
	\sectionfont{\color{\titlecolor}} 
	\subsectionfont{\color{\titlecolor}} 
	\paragraphfont{\color{\titlecolor}} 
}

% ========== Index ==========
% Fix up index spacing (TODO: how so?)
% This package seems to mess up title page for twocolumn articles for some reason, so make conditional.
\iftoggle{bookHeader}{\RequirePackage{idxlayout}}{} 



% ========== Macros ==========
\iftoggle{macros}{    \RequirePackage{bespoke6macros}    }{}


