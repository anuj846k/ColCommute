import { type NextRequest, NextResponse } from "next/server";

export async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  if (pathname.startsWith("/ping")) {
    return new Response("pong", { status: 200 });
  }

  const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
  const token = request.cookies.get("unified_access_token")?.value ?? null;

  // If already authenticated, keep auth screens inaccessible.
  if (token && ["/login", "/register"].includes(pathname)) {
    return NextResponse.redirect(new URL(`${base}/`, request.url));
  }

  // For all other pages, require an auth token.
  if (!token && !["/login", "/register"].includes(pathname)) {
    return NextResponse.redirect(new URL(`${base}/login`, request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/",
    "/chat/:id",
    "/api/:path*",
    "/login",
    "/register",

    "/((?!_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)",
  ],
};
